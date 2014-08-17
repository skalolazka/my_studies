#!/usr/bin/perl

# task: queue with max, any series of enqueue + dequeue + max = O(n)
# works only if there are no duplicates in the queue!!!

use strict;
use warnings;

package MyQueue;

my $size = 9; # leave it=)

sub new {
    my ($class, @values) = @_;
    my $self = { values => [map {undef} (0..$size)], start => undef, end => 0, max => [] };
    bless $self => $class;
    for my $value (@values) { # this is not the main concern here, so even though I know it's not optimal, let me leave it as it is here
# could have just left an implementation with no values accepted in new()
        $self->enqueue($value);
    }
    return $self;
}

sub resize { # again, this is not the main concern here
    my $self = shift;
    $self->{values} = [@{$self->{values}}, map {undef} (0..scalar(@{$self->{values}})-1)];
}

sub enqueue {
    my ($self, $value) = @_;
    $self->{start} = 0 unless defined($self->{start});
    if ($self->{end} == scalar(@{$self->{values}})) {
        $self->resize();
    }
    $self->{values}[$self->{end}] = $value;
    if (!defined($self->max) || $value >= $self->max) {
        $self->{max} = [$value];
    }
    else {
        push(@{$self->{max}}, $value);
    }
    $self->{end}++;
}

sub lookup {
    my $self = shift;
    if (!defined($self->{start}) || $self->{start} == $self->{end}) {
        return undef;
    }
    else {
        return $self->{values}[$self->{start}];
    }
}

sub dequeue {
    my $self = shift;
    my $elem = $self->lookup;
    return undef unless defined($elem);
    $self->{start}++;
    my $next = $self->lookup;
    if ($elem == $self->max && (!defined($next) || $next < $self->max)) {
        shift(@{$self->{max}});
    }
    return $elem;
}

sub max {
    my $self = shift;
    return $self->{max}[0];
}

package TestMyQueue;

use Test::More;
use Test::Deep;
use Data::Dumper;

my $q = MyQueue->new(4);
is_deeply($q->{max}, [4], 'max set');
is($q->max, 4, 'max ok');
$q->enqueue(2);
is_deeply($q->{max}, [4,2], 'max added');
is($q->max, 4, 'max ok');
$q->enqueue(1);
is_deeply($q->{max}, [4,2,1], 'max added again');
is($q->max, 4, 'max ok');
$q->enqueue(3);
is_deeply($q->{max}, [4,2,1,3], 'max added even more');
is($q->max, 4, 'max ok');
$q->enqueue(5);
is_deeply($q->{max}, [5], 'max cut down');
is($q->max, 5, 'max ok');
$q = MyQueue->new(4,2,1,5,7,3);
is($q->max, 7, 'max ok from start');
$q->dequeue();
is($q->max, 7, 'max still same');
$q->dequeue();
$q->dequeue();
$q->dequeue();
$q->dequeue();
is($q->max, 3, 'max changed');
$q->dequeue();
is($q->max, undef, 'no items left');
$q->enqueue(10);
is($q->max, 10, 'max started');

done_testing;
