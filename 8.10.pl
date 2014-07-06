#!/usr/bin/perl

use strict;
use warnings;

package MyQueue;

sub new {
    my ($class, $capacity) = @_;
    return unless defined($capacity); # let us have no defaults
    my $self = { values => [map {undef} (0..$capacity-1)], start => -1, end => -1 };
    # 'tis funny, but in perl's (0..$x) $x is included
    return bless $self => $class;
}

sub resize {
    my $self = shift;
    $self->{values} = [@{$self->{values}}, map {undef} (0..scalar(@{$self->{values}}))];
    # well, I have read in a cool article that it's the common practice - to double the size in resizing
}

sub enqueue {
    my ($self, $value) = @_;
    $self->{start} = 0 if $self->{start} == -1;
    $self->{end}++;
    if ($self->{end} == scalar(@{$self->{values}})) {
        $self->resize();
    }
    $self->{values}[$self->{end}] = $value;
}

sub dequeue {
    my $self = shift;
    return undef if $self->{start} == -1 || $self->{start} > $self->{end};
    my $elem = $self->{values}[$self->{start}];
    $self->{start}++;
    return $elem;
}

sub size {
    my $self = shift;
    return 0 if $self->{start} == -1;
    return $self->{end} - $self->{start} + 1;
}

package TestMyQueue;

use Test::More;
use Test::Deep;

my $q = MyQueue->new(5); # 5 - capacity
is_deeply($q, {'values' => [map {undef} (1..5)], end => -1, start => -1}, 'created with capacity 5');
$q = MyQueue->new(2); # 2 - capacity
use Data::Dumper;
#warn Dumper($q);
is_deeply($q, {'values' => [undef, undef], end => -1, start => -1}, 'created with capacity 2');
is($q->size(), 0, 'size 0 after init');
$q->enqueue(4);
is_deeply($q, {'values' => [4,undef], 'end' => 0, 'start' => 0}, 'enqueue once');
is($q->size(), 1, 'size 1');
$q->enqueue(5);
is_deeply($q, {'values' => [4,5], 'end' => 1, 'start' => 0}, 'enqueue again');
is($q->size(), 2, 'size 2');
$q->enqueue(6);
is_deeply($q, {'values' => [4,5,6,undef,undef], 'end' => 2, 'start' => 0}, 'enqueue third time - resize');
is($q->size(), 3, 'size 3');
is($q->dequeue(), 4, 'dequeue');
is_deeply($q, {'values' => [4,5,6,undef,undef], 'end' => 2, 'start' => 1}, 'after dequeue');
is($q->size(), 2, 'size changed after dequeue');
$q->enqueue(7);
is_deeply($q, {'values' => [4,5,6,7,undef], 'end' => 3, 'start' => 1}, 'enqueue more');
is($q->dequeue(), 5, 'dequeue now');
is($q->dequeue(), 6, 'dequeue again');
is($q->dequeue(), 7, 'dequeue again and again');
is_deeply($q, {'values' => [4,5,6,7,undef], 'end' => 3, 'start' => 4}, 'after dequeues');
is($q->dequeue(), undef, 'nothing to dequeue');
is($q->dequeue(), undef, 'still nothing to dequeue');
is($q->size(), 0, 'size 0 again');
is_deeply($q, {'values' => [4,5,6,7,undef], 'end' => 3, 'start' => 4}, 'after empty dequeues');
$q->enqueue(8);
is_deeply($q, {'values' => [4,5,6,7,8], 'end' => 4, 'start' => 4}, 'added 8');
is($q->dequeue(), 8, 'dequeued 8');
is($q->size(), 0, 'size 0');

done_testing;
